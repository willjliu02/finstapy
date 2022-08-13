from finstapy import FinstaPy

import time

fp1 = FinstaPy('finstapy2022', 'neu2025')
fp1.log_in()
fp1.dismiss_notification()
fp1.find_hashtag("love")

time.sleep(10)

fp1.quit()