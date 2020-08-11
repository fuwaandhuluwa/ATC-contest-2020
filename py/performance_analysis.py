

#   using cProfile library and snakeviz module visualization results

#  -------------------------------------------------------------
#  First step :
#       using cProfiler to run application
#  -------------------------------------------------------------

# import cProfile
#
# cProfile.run('run(readFileContent("C:/Users/jiafu.li/PyCharmProjects/AStar_Algorithm/testcase/17.in"))',
#              filename='status.txt', sort='cumulative')


#  -------------------------------------------------------------
#  Second step:
#        using snakeviz tool to visualize the results and find
#        out which function takes up more resources
#  -------------------------------------------------------------

# below command must be used in shell
# snakeviz status.txt


# from line_profiler import LineProfiler
# lp = LineProfiler()
# lp_wrapper = lp(run)
# lp_wrapper(readFileContent("C:/Users/jiafu.li/PyCharmProjects/AStar_Algorithm/testcase/1.in"))
# lp.print_stats()
