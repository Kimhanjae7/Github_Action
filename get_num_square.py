improt os

num = os.environ.get("INPUT.NUM")

if num:
    try:
       num = int(num)
    except Exception:
       exit()
else:
   num = 1
    
print(f"::set-output name=num_squared::{num**2}")
