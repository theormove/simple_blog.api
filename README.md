# simple blog api
# Stack
Python 3.8
Django 4.1 
Django Rest Framework
# Endpoints
## api/register (Register New User)
{
"username": string
"password": string
}
## api/token (get JWT token)
{
"username": string
"password": string
}
## api/post/create
{
"title":string
"content":string
"author":int(user id)
}
## api/post/{ID}/like (Like or Dislike if already liked post with id = ID. Need to provide JWT for this )
{}
## api/activity/{USERNAME} (Last activity and login)
## api/analytics/?date_from=YYYY-MM-DD&date_to=YYYY-MM-DD& (total number of likes)
# To run yourself install packages from requirements.txt
