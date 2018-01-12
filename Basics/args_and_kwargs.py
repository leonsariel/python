# _*_ coding: utf-8 _*_
__author__ = 'Di Meng'
__date__ = '1/12/2018 4:16 PM'


def args_function(*args):
    """test with args

    :param args: any normal param eg 1,2, "hello"
    :return: None
    """
    for arg in args:
        print(arg)


def kwargs_function(**kwargs):
    """test with kwargs

    :param kwargs: default para eg. x=1 ; kwargs is dictionary
    :return: none
    """


    for i in kwargs:
        print(kwargs[i])

def mix_args_and_kwargs(*args, **kwargs):
    """Mix using args and kwargs

    :param args: normal args
    :param kwargs: key words
    :return: None
    """
    for i in args:
        print(i)
    for j in kwargs:
        print("keywords: ", kwargs[j])


kwargs_function(x=1,y=2)

# must args first then kwargs
mix_args_and_kwargs(1,2,3, x=2)