import os

class PackageVersionProvider:
    def __init__(self):
        self.version = None

    def get_version(self):
        if self.version is None:
            try:
                this_directory = os.path.abspath(os.path.dirname(__file__))
                with open(os.path.join(this_directory, '..', 'VERSION')) as version_file:
                    self.version = version_file.read().strip()
            except Exception as e:
                return 'InvalidPackageVersion'
            
        return self.version
            