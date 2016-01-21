import os

def find_dupes(root_dir):
    """Find duplicate files in the root and all subdirectories.
    Returns a list of lists, where each sublist is a duplicate file."""
    # comparing files of equivalent size
    # create a dictionary where key = filesize, value = list of files         of that size
    filesizes = {}
    
    #filesize[size].append(filename) # 'filesize[40] --> [filename1, filename2, ...] 
    

    
    # find all subfiles chrdir (tree of directories)
    all_files = os.listdir(root_dir)
    # for all_file in all_files:
        # if all_file.isdir():
            # sub_dir
            
    # assuming listdir returns a tree, which it doesn't
    tree = os.listdir(root_dir)
    # depth first search --> stack
    # keep track of nodes to visit, add children to stack, and pop off     and repeat
    curr_node = tree.root
    to_visit = []
    while curr_node:
        if curr_node.children: # children are subdirectories
            to_visit.extend(curr_node.children)
        # check all files in current directory
        all_files = os.listdir(curr_node)

        # adding files to dictionary comparing contents
        for all_file in all_files:
            if not all_file.isdir():
                # get current file's size
                curr_size = all_file.size()
                if filesizes.get(curr_size, 0) != 0:
                    filesizes[curr_size].append(all_file)
                else:
                    filesizes[curr_size] = [all_file]
                
        # get next node
        curr_node = to_visit.pop()
        
    # return all values where list has more than one item
    duplicate_results = []
    for key, val in filesizes:
        if len(val) > 1:
            duplicate_results.append(val)
            
    return duplicate_results
        
    
    
    # filecontents = {}
    # contents = filename1.contents
    # if filecontents.get(contents, 0) != 0: # file contents already exist therefore, duplicate
    #     filecontents[contents].append(filename1)
        
        
        
    # 'apple' --> ###7 'berry' --> ###2 'cherry' ---> ###2
    
#     with open(root_dir, rw+) as my_file:
#         my_file.readline()
        
#         my_file.close()
        
    
    

# find_dupes('/foo') =>
# 
# [
#    ['/foo/bar.png', '/foo/images/foo.png'],
#    ['/foo/file.tmp', '/foo/other.temp', '/foo/temp/baz/that.foo']
# ]

