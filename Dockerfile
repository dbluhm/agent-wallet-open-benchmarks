FROM bcgovimages/von-image:py36-1.16-1
RUN pip install aries-askar
COPY ./test_askar.py /home/indy/test_askar.py
COPY ./test_indy.py /home/indy/test_indy.py
CMD ["python", "test_indy.py"]
