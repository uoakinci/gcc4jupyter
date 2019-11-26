
##### Usage

- Load Extension
> `%load_ext gcc_plugin`

- Mark a cell to be treated as cuda cell
> `%%gcc --name example.cpp --compile false`
>> NOTE: The cell must contain either code or comments to be run successfully. 
>> It accepts 2 arguments. `-n` | `--name`  - which is the name of either Source or Header
>> The name parameter must have extension `.cpp`, `.c` or `.h`
>> Second argument `-c` | `--compile`; default value is `false`. The argument is a flag to specify
>> if the cell will be compiled and run right away or not. It might be usefull if you're playing in
>> the `main` function

- To compile and run all CUDA files you need to run
```
%%gcc_run
# This line just to bypass an exeption and can contain any text
```
