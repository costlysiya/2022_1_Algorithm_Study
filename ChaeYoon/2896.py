mine=[int(n) for n in input().split()]
ratio=[int(n) for n in input().split()]
cup=min(mine[0]/ratio[0],mine[1]/ratio[1],mine[2]/ratio[2])
print(mine[0]-(ratio[0]*cup),mine[1]-(ratio[1]*cup),mine[2]-(ratio[2]*cup))

