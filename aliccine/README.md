#load dummy data into the application
python3 manage.py update_db

#Get API response data and cache it into CDN
python3 manage.py  update_api_cache



#Update config under this file:
> settings.yaml


#Endpoints
>  api/v1/food/
>  admin/