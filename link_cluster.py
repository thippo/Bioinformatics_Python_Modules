def link_cluster(link_list_list):
    first_pair = link_list_list.pop(0)
    cluster_list_list_list = []
    cluster_one_list_list = [first_pair]
    cluster_dict = {}
    cluster_dict[first_pair[0]]=1
    cluster_dict[first_pair[1]]=1
    pop_list = []
    n_boolen = True
    while link_list_list:
        if n_boolen:
            n_boolen = False
            for i in range(len(link_list_list)):
                if link_list_list[i][0] in cluster_dict.keys() or link_list_list[i][1] in cluster_dict.keys():
                    cluster_one_list_list.append(link_list_list[i])
                    cluster_dict[link_list_list[i][0]]=1
                    cluster_dict[link_list_list[i][1]]=1
                    pop_list.append(i)
                    n_boolen = True
            for i in pop_list[::-1]:
                link_list_list.pop(i)
            pop_list = []
        else:
            cluster_list_list_list.append(cluster_one_list_list)
            cluster_one_list_list = []
            cluster_dict = {}
            n_boolen = True
            first_pair = link_list_list.pop(0)
            cluster_one_list_list.append(first_pair)
            cluster_dict[first_pair[0]]=1
            cluster_dict[first_pair[1]]=1
    cluster_list_list_list.append(cluster_one_list_list)
    return cluster_list_list_list