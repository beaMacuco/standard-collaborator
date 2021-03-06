from dye.tasklib.django import _manage_py


def post_deploy(environment):
    """ This function is called by the main deploy in dye/tasklib after
    all the other tasks are done.  So this is the place where you can
    add any custom tasks that your project requires, such as creating
    directories, setting permissions etc."""
    build_webassets()


def build_webassets():
    _manage_py(['assets', 'clean'])
    _manage_py(['assets', 'build'])
