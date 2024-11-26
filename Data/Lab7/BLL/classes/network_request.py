"""Does all the network requests"""
import re
import requests
import global_variables


class NetworkRequest:
    """The class that does the network requests"""
    @staticmethod
    def get(uow, entity, db_handler):
        """Sends a GET request"""
        prompt = input("1 - GET all\n2 - GET by ID\nYour choice: ")
        try:
            if prompt == "1":
                result = getattr(uow, entity).get_all()
                db_handler.insert_history(entity, "GET", "all")
                return result
            if prompt == "2":
                entity_id = input("Enter ID: ")
                result = getattr(uow, entity).get_by_id(entity_id)
                db_handler.insert_history(entity, "GET", entity_id)
                return [result]
            print("Invalid input!")
        except requests.HTTPError as e:
            raise requests.HTTPError(f"An error occurred: {e}")
        return []

    @staticmethod
    def post(uow, entity, db_handler):
        """Sends a POST request with the new data"""
        try:
            example = getattr(uow, entity).get_by_id(1)
            request = NetworkRequest.form_request("", example)
            result = getattr(uow, entity).add(request)
            db_handler.insert_history(entity, "POST", result["id"])
            print(f"Created successfully with ID: {result['id']}")
        except ValueError as e:
            print(e)
        except requests.HTTPError as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def patch(uow, entity, db_handler):
        """Sends a PATCH request with the updated data"""
        entity_id = input("Enter ID: ")
        try:
            example = getattr(uow, entity).get_by_id(entity_id)
            NetworkRequest.form_request("", example, is_post_request=False)
            db_handler.insert_history(entity, "PATCH", entity_id)
            print(f"Updated successfully for ID: {entity_id}")
        except ValueError as e:
            print(e)
        except requests.HTTPError as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def delete(uow, entity, db_handler):
        """Sends a DELETE request"""
        entity_id = input("Enter ID: ")
        try:
            if getattr(uow, entity).delete(entity_id):
                db_handler.insert_history(entity, "DELETE", entity_id)
                print("Deleted successfully.")
        except requests.HTTPError as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def form_request(link, data, is_post_request=True):
        """Forms a request for POST and PATCH requests"""
        request = {}
        for key, item in data.items():
            if isinstance(item, dict):
                request[key] = NetworkRequest.form_request(link, item, is_post_request)
            elif key != "id":
                prompt_1 = input("Enter " + key + ": ")
                if prompt_1.strip() != "":
                    if "id" in key.lower():
                        prompt_1 = int(prompt_1)
                    elif (key.lower() == "email"
                          and not re.match(global_variables.EMAIL_REGEX, prompt_1)):
                        raise ValueError("The email value is incorrect!")
                    elif ((key.lower() == "url" or key.lower() == "website")
                          and not re.match(global_variables.LINK_REGEX, prompt_1)):
                        raise ValueError("The website value is incorrect!")
                    elif (key.lower() == "phone"
                          and not re.match(global_variables.PHONE_REGEX, prompt_1)):
                        raise ValueError("The phone value is incorrect!")
                    elif key.lower() == "lat" and not -90 <= int(prompt_1) <= 90:
                        raise ValueError("The latitude value is incorrect!")
                    elif key.lower() == "lng" and  not -180 <= int(prompt_1) <= 180:
                        raise ValueError("The longitude value is incorrect!")
                    request[key] = prompt_1
                else:
                    if is_post_request:
                        raise ValueError("The value cannot be empty!")
        return request
