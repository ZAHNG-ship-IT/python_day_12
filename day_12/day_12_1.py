print("{},{},{}".format('张','三','五'))

###.format()函数作用是类似于补充占位符的作用

print('{1} 和 {0}'.format('Google', 'Runoob'))

####但是，补充的占位符是有顺序的，可以动态调换顺序的

print('{name}网址： {site}'.format(site='hihi',name='张成富',))

####类似与字典的方式吧，键值


# 位置及关键字参数可以任意的结合


###使用.format()的话，对传入{}内部的东西，可以直接进行转化，如!ascii,!ord,!reqr等等
###同时  :   ,这个可以规定传入东西的长度
print('！！！！{0:.10000d}'.format(10))
