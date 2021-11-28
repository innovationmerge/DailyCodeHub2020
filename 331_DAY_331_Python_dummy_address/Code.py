# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Dummy Data Generation in Python

# Python program generate dummy address

from faker import Faker
fake = Faker("en_US")
for _ in range(10):
    print(fake.address())


""" 
# Output : 
    189 Carney Circles
    Frankfurt, CA 99389
    156 Kelli Fall
    East Jenniferport, CO 17673       
    897 Kennedy Lights Apt. 850       
    Thomasmouth, SD 93337
    90473 Thomas Glens
    Hollyfort, OK 80761
    745 Brady Prairie
    North Dominique, IL 42118
    USNV Fowler
    FPO AA 05390
    66782 Leslie Plains
    Banksville, WI 04771
    608 Kennedy Roads Apt. 597        
    Port Heather, OK 91578
    03193 Thompson Brook
    Carterbury, NV 95837
    49896 Sharon Pine Suite 828       
    Odonnellview, WY 39579
"""

