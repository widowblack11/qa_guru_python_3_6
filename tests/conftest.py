import glob
import os

import pytest

from tests.test_for_zip import path_to_the_created_archive


@pytest.fixture()
def cleaning_the_directory_before_the_test():
    path_file = os.path.join(path_to_the_created_archive, '*.zip*')
    for file in glob.glob(path_file):
        os.remove(file)


if __name__ == '__main__':
    cleaning_the_directory_before_the_test()
