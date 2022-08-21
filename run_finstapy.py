from finstapy import FinstaPy

import time

fp1 = FinstaPy('finstapy2022', 'neu2025', ["This is amazing!", "That's awesome"], 
                ["#coding", "#codingisfun", "webdeveloper", "html", "css", "programmer", "coder"])
                
homePage = fp1.go_to_home_page()
for i in range(5):
    print(f"Scroll {i}:")
    fp1.view_page(homePage)

time.sleep(60)
fp1.quit()