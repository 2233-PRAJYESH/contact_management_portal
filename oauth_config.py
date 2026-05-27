from authlib.integrations.flask_client import OAuth


oauth = OAuth()


google = oauth.register(

    name="google",

    client_id=None,

    client_secret=None,

    server_metadata_url=
    "https://accounts.google.com/.well-known/openid-configuration",

    client_kwargs={
        "scope": "openid email profile"
    }
)