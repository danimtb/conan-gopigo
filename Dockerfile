FROM conanio/gcc6-armv7hf

RUN pip install conan --upgrade
RUN pip install conan_package_tools
USER root
ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
