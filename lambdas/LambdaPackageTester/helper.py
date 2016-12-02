list1 = [str(x) for x in xrange(0,10)]


def helper(me):
    print('{} needs help'.format(me))
    print('here is a list {}'.format(",".join(list1)))