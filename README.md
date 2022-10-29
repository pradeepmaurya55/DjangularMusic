# DjangularMusic
##### A music streaming website based of Django and Angular 
This is backend part of the website.

##  API
    The following API endpoints are available.
    Note : Protected URLs(endpoints) need Access token to be passed as in Authorization Header.
#### Get list of all songs
##### Request
`GET /api/v1/songs/`
##### Response
    [
        {"id": 1,"title": "haru no Katami","artist": "Chitose Hajime","uploader": 1,"album": "/media/songs/album/900-Drizzt-l.jpg"},
        {
            "id": 2,
            "title": "Sohni",
            "artist": "Prophec Ft. Deep C",
            "uploader": 1,
            "album": "/media/songs/album/AlbumArtSmall.jpg"
        },
        {
            "id": 3,
            "title": "Let's Dance",
            "artist": "Bombay Rockers",
            "uploader": 1,
            "album": "/media/songs/album/AlbumArtSmall_mZzymQi.jpg"
        }
    ]
#### Get all details of a particular song 
##### Request
`GET /api/v1/songs/<id>`_[protected]_
<id> is the id of song

Example url:

    ../api/v1/songs/1 
##### Response
    {
        "id": 1,
        "title": "haru no Katami",
        "artist": "Chitose Hajime",
        "song": "/media/songs/tracks/fharu-no-katami.mp3",
        "uploader": 1,
        "album": "/media/songs/album/900-Drizzt-l.jpg"
    }

#### Register a user
##### Request
`GET /api/user/register`

Example:

    Request Body:
        {
        "email":"a@djangular.com",
        "password":"pcsxe",
        "password2":"pcsxe"
        }
##### Response
    {
        "msg": "Registration Successful"
    }
    
#### Login a user
##### Request
`GET /api/user/login`

Example:

    Request body :
        {
        "email":"a@djangular.com",
        "password":"pcsxe",
        }
##### Response
    {
        "token": {
            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NzE1MTg3MywiaWF0IjoxNjY3MDY1NDczLCJqdGkiOiI2ZjNlMTJjMjlkMDg0NmU0YmI3MWY3MWNmMzAzZmEzMiIsInVzZXJfaWQiOjV9.Bf9IVpUQVhmHJG6o3PnsuMB5xhDBuBmcDYvR58fibXM",
            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3MDY2NjczLCJpYXQiOjE2NjcwNjU0NzMsImp0aSI6IjA0YTJiZWQ1ZjY4NjQ2NTk5YmU1ZjM5NDc3OWY5YzZkIiwidXNlcl9pZCI6NX0.fBllB9anpg4b1mGYvOcc8TYe-uSAPPH-GXdiZC6FwYk"
        },
        "msg": "Login Successful"
    }
    
#### Get user profile details
##### Request
`GET /api/user/profile` _[protected]_
Example:

    Request Header:
        Key:Authorization
        Value:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3MDY2NjczLCJpYXQiOjE2NjcwNjU0NzMsImp0aSI6IjA0YTJiZWQ1ZjY4NjQ2NTk5YmU1ZjM5NDc3OWY5YzZkIiwidXNlcl9pZCI6NX0.fBllB9anpg4b1mGYvOcc8TYe-uSAPPH-GXdiZC6FwYk

##### Response

    {
        "id": 5,
        "email": "a@djangular.com",
        "name": null,
        "avatar": "/media/user.png"
    }

#### Change password
##### Request
`GET /api/user/changepassword` _[protected]_
Example:

    Request Body:
        {
            "password":"pcsxe2",
            "password2":"pcsxe2",
            "old_password":"pcsxe"
        }

    Request Header:
        Key:Authorization
        Value:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3MDY3MTAxLCJpYXQiOjE2NjcwNjU5MDEsImp0aSI6ImY2ZGYyM2Y3Y2EwZjQ3N2I5ZWRiOWU4OTA1NTcyMjBhIiwidXNlcl9pZCI6NX0.R_HeGvKFHY-1b2OPbaPgMpsHUBhHY9uZ1t_QHLkeOHo

##### Response

    {
        "msg": "Password Change Successful"
    }
