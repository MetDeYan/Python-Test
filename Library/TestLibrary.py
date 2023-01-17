import requests
import logging


logging.basicConfig(level=logging.INFO, filename="../log/py_log.log",
                    format="%(asctime)s %(levelname)s %(message)s")


def create_body(dateStart, dateEnd, education, results):
    body = {"dateStart": dateStart, "dateEnd": dateEnd, "education": education, "results": results}
    return body


def add_new_education(education_api, education_body):
    response = requests.post(education_api, json=education_body).json()
    logging.info("Add new education")
    return response


def get_response(education_api):
    response = requests.get(education_api).json()
    logging.info("Get user educations")
    return response["rows"]


def check_new_education(response, education_id):
    for item in response:
        if item["id"] == education_id["id"]:
            return True
    return False


def check_the_education_value(response, education):
    for item in response:
        if item["education"] == education:
            return True
    return False


def check_the_results_value(response, results):
    for item in response:
        if item["results"] == results:
            return True
    return False


def check_response():
    api_url = "http://localhost:3000/api/employees/34263d5c-7332-11ec-aa3e-0242ac11000a/education"
    response = requests.get(api_url).status_code
    logging.info("Get user educations")
    return response
