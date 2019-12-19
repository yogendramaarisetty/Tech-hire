def compile_run(language,code,custom_input,request):
    output=""
    if language == "Python":
        output = execute_python(code,custom_input)
    elif language == "Java":
        output = execute_java(code,custom_input)
    elif language == "C":
        output = execute_c(code,custom_input)
    elif language == "C++":
        output = execute_cpp(code,custom_input)
    elif language == "C#":
        output = execute_csharp(code,custom_input)
    return output+' '+str(request.user.id)+' '+request.user.username

def execute_python(code,custom_input):
    return "this is python output"
def execute_java(code,custom_input):
    return "this is java output"
def execute_c(code,custom_input):
    return "this is C output"
def execute_cpp(code,custom_input):
    return "this is C++ output"
def execute_csharp(code,custom_input):
    return "this is C# output"
