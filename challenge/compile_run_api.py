import subprocess,os
from subprocess import run, PIPE,STDOUT,Popen

def compile_run(language,code,custom_input,request):
    output=""
    file_name = request.user.username+str(request.user.id)
    path = os.getcwd()+"\\code_files"
    if language == "Python":
        output = execute_python(code,custom_input,file_name,path)
    elif language == "Java":
        output = execute_java(code,custom_input,file_name,path)
    elif language == "C":
        output = execute_c(code,custom_input,file_name,path)
    elif language == "C++":
        output = execute_cpp(code,custom_input,file_name,path)
    elif language == "C#":
        output = execute_csharp(code,custom_input,file_name,path)
    return output

def execute_python(code,custom_input,file_name,path):
    root_path = os.getcwd()
    path= os.path.join(path,'python_codes')
    os.chdir(f'{path}')
    try:
        os.mkdir(file_name)
    except:
        pass
    path= os.path.join(path,file_name)
    os.chdir(path)
    file_name_ext= file_name+".py"
    code_file = open(f'{file_name_ext}','w')
    code_file.flush()
    file_lines = code.split("\n")
    for l in file_lines:
        code_file.write(l+"\n")
    code_file.close()
    cmd = f'py {file_name_ext}'
    p=os.getcwd()
    run_code = subprocess.run(cmd, stdout=PIPE,input=custom_input, stderr=subprocess.PIPE,encoding='ascii',shell=True)
    errors = run_code.stderr
    if len(errors)==0:
        os.chdir(root_path)
        return run_code.stdout
    else:
        os.chdir(root_path)
        return errors   

def execute_java(code,custom_input,file_name,path):
    root_path = os.getcwd()
    path= os.path.join(path,'java_codes')
    os.chdir(f'{path}')
    try:
        os.mkdir(file_name)
    except:
        pass
    path= os.path.join(path,file_name)
    os.chdir(path)
    file_name_ext= "MyClass.java"
    code_file = open(f'{file_name_ext}','w')
    code_file.flush()
    file_lines = code.split("\n")
    for l in file_lines:
        code_file.write(l+"\n")
    code_file.close()
    cmd = f'g++ {file_name_ext}'
    p=os.getcwd()
    compile_code = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    errors = compile_code.stderr.readlines()
    if len(errors)==0:
        run_code = subprocess.run("a", stdout=PIPE,input=custom_input, stderr=subprocess.PIPE,encoding='ascii',shell=True)
        os.chdir(root_path)
        return run_code.stdout
    else:
        error=""
        for e in errors:
            error+=e.decode("utf-8")
        os.chdir(root_path)
        return error 


def execute_c(code,custom_input,file_name,path):
    root_path = os.getcwd()
    path= os.path.join(path,'c_codes')
    os.chdir(f'{path}')
    try:
        os.mkdir(file_name)
    except:
        pass
    path= os.path.join(path,file_name)
    os.chdir(path)
    file_name_ext= file_name+".c"
    code_file = open(f'{file_name_ext}','w')
    code_file.flush()
    file_lines = code.split("\n")
    for l in file_lines:
        code_file.write(l+"\n")
    code_file.close()
    cmd = f'gcc {file_name_ext}'
    p=os.getcwd()
    compile_code = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    errors = compile_code.stderr.readlines()
    if len(errors)==0:
        run_code = subprocess.run("a", stdout=PIPE,input=custom_input, stderr=subprocess.PIPE,encoding='ascii',shell=True)
        os.chdir(root_path)
        return run_code.stdout
    else:
        error=""
        for e in errors:
            error+=e.decode("utf-8")
        os.chdir(root_path)
        return error   

def execute_cpp(code,custom_input,file_name,path):
    root_path = os.getcwd()
    path= os.path.join(path,'cpp_codes')
    os.chdir(f'{path}')
    try:
        os.mkdir(file_name)
    except:
        pass
    path= os.path.join(path,file_name)
    os.chdir(path)
    file_name_ext= file_name+".cpp"
    code_file = open(f'{file_name_ext}','w')
    code_file.flush()
    file_lines = code.split("\n")
    for l in file_lines:
        code_file.write(l+"\n")
    code_file.close()
    cmd = f'g++ {file_name_ext}'
    p=os.getcwd()
    compile_code = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    errors = compile_code.stderr.readlines()
    if len(errors)==0:
        run_code = subprocess.run("a", stdout=PIPE,input=custom_input, stderr=subprocess.PIPE,encoding='ascii',shell=True)
        os.chdir(root_path)
        return run_code.stdout
    else:
        error=""
        for e in errors:
            error+=e.decode("utf-8")
        os.chdir(root_path)
        return error 

def execute_csharp(code,custom_input,file_name):
    root_path = os.getcwd()
    path= os.path.join(path,'csharp_codes')
    os.chdir(f'{path}')
    try:
        os.mkdir(file_name)
    except:
        pass
    path= os.path.join(path,file_name)
    os.chdir(path)
    file_name_ext= file_name+".cs"
    code_file = open(f'{file_name_ext}','w')
    code_file.flush()
    file_lines = code.split("\n")
    for l in file_lines:
        code_file.write(l+"\n")
    code_file.close()
    cmd = f'g++ {file_name_ext}'
    p=os.getcwd()
    compile_code = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    errors = compile_code.stderr.readlines()
    if len(errors)==0:
        run_code = subprocess.run("a", stdout=PIPE,input=custom_input, stderr=subprocess.PIPE,encoding='ascii',shell=True)
        os.chdir(root_path)
        return run_code.stdout
    else:
        error=""
        for e in errors:
            error+=e.decode("utf-8")
        os.chdir(root_path)
        return error 
