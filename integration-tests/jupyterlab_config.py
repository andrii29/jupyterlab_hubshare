from IPython.html.services.contents.filemanager import FileContentsManager

c.ServerApp.jpserver_extensions = {"jupyterlab_hubshare": True}
c.HubShare.file_path_template = "{path}"
c.HubShare.use_jupyterhub_redirect = False
