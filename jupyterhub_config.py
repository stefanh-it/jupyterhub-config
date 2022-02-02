# /etc/jupyterhub/jupyterhub_config.py
# PAM Authenticator

# Force the proxy to only listen to connections to 127.0.0.1 (on port 8000)
c.JupyterHub.bind_url = 'http://127.0.0.1:8000'

#c = get_config()
c.JupyterHub.log_level = 10
c.Spawner.cmd = '/var/jupyterhub/jupytervenv/bin/jupyter-notebook'

# Cookie Secret Files
#c.JupyterHub.cookie_secret_file = 'jupyterhub_cookie_secret'
#c.ConfigurableHTTPProxy.auth_token = 'proxy_auth_token'

# Users
c.Authenticator.whitelist = {'arch'}
c.Authenticator.admin_users = {'arch'}