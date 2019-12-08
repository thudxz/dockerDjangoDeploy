from celery.decorators import task
import time

@task(name="For test", bind=True)
def reportTest(self):
  time.sleep(5)
  self.update_state(meta={"name": "one", "status": "running"})
  time.sleep(5)
  self.update_state(meta={"name": "two", "status": "running"})
  