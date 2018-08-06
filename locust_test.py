from locust import HttpLocust, TaskSet, task
class WebsiteTasks(TaskSet):
	@task(1)
	def index(self):
		with self.client.get("/?act=game_stars",catch_response = True) as response:
			if response.status_code != 200:
				response.failure('Fail')
			else:
				response.success()
class WebsiteUser(HttpLocust):
	host = 'http://9test74-wap.stg3.1768.com'
	task_set = WebsiteTasks
	min_wait = 50
	max_wait = 150
