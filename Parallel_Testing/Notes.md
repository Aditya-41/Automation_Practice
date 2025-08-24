# Python Parallel Testing

* Install the pytest-xdist
    ```cmd
    pip install pytest-xdist
    ```

* Add udid and systemPort in Desired Capabilities

* Run the file ising command as :
    pytest -n <numprocesses>
    ex :- pytest -n=2  (For two devices)