from Course import Course
from bs4 import BeautifulSoup
import requests

class Course:
    def __init__(self, title, schedule, description):
        self.title = title
        self.schedule = schedule
        self.description = description

    def __str__(self):
        output = ''
        output += f"Title: {self.title}\nSchedule: {self.schedule}\nDescription: {self.description}\n"
        output += '------------------'
        return output

    def get_courses(self):
        return self.get_page().select('.post')

    def make_courses(self):
        for course in self.get_page().select('.post'):
            title = course.select("h2")[0].text if course.select("h2") else ''
            date = course.select(".date")[0].text if course.select(".date") else ''
            description = course.select("p")[0].text if course.select("p") else ''

            new_course = Course(title, date, description)
            self.courses.append(new_course)
        return self.courses
