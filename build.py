from conan.packager import ConanMultiPackager
import os, re


def get_value_from_recipe(search_string):
    with open("conanfile.py", "r") as conanfile:
        contents = conanfile.read()
        result = re.search(search_string, contents)
    return result

def get_name_from_recipe():
    return get_value_from_recipe(r'''name\s*=\s*["'](\S*)["']''').groups()[0]

def get_version_from_recipe():
    return get_value_from_recipe(r'''version\s*=\s*["'](\S*)["']''').groups()[0]


if __name__ == "__main__":
    name = get_name_from_recipe()
    version = get_version_from_recipe()
    reference = "{0}/{1}".format(name, version)
    conan_username = "conan"
    conan_channel = "stable"
    login_username = "czoido"
    upload_remote = "https://api.bintray.com/conan/czoido/conan-packages"

    builder = ConanMultiPackager(
        username=conan_username,
        channel=conan_channel,
        login_username=login_username,
        reference=reference,
        archs=["armv7hf"],
        gcc_versions=["8"],
        upload=upload_remote,
        remotes=upload_remote
        )

    builder.add_common_builds()
    builder.run()