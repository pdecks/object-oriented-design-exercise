"""our function will walk through the file system, store files in a dictionary,
and identify the more recently edited file as the copied one when it finds a
duplicate.

We're going to make our function iterative instead of recursive to avoid stack
overflow 
"""

import os
import hashlib

def find_duplicate_files(starting_directory='./tmp/test'):
    files_seen_already = {}
    stack = [starting_directory]

    # track tuples of (duplicate_file, original file)
    duplicates = []

    while len(stack) > 0:

        current_path = stack.pop()

        # if path is a directory, put the contents in our stack
        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
                stack.append(full_path)

        # if path is a file
    else:
        # get its hash
        file_hash = sample_hash_file(current_path)

        # get its last edited time
        # getmtime: Return the time of last modification of path.
        current_last_edited_time = os.path.getmtime(current_path)

        # seen file before
        if files_seen_already.get(file_hash, 0) != 0:
            existing_last_edited_time, existing_path = files_seen_already[file_hash]

            # current file is a duplicate
            if current_last_edited_time > existing_last_edited_time:
                duplicates.append((current_path, existing_path))
            # existing file is duplicate
            else:
                duplicates.append((existing_path, current_path))
                # update dictionary with new file's info
                files_seen_already[file_hash] = \
                    (current_last_edited_time, current_path)

        # new file - add to dictionary
        else:
            files_seen_already[file_hash] = \
                (current_last_edited_time, current_path)

    return duplicates


def sample_hash_file(path):
    """We would like to store a constant-size "fingerprint" of the file in our
    dictionary, instead of the whole file itself.

    For each file, we have to look at every bit that the file occupies in order
    to hash it and take a "fingerprint." That is why our time cost is high. Can
    we fingerprint a file in constant time instead?

    What if instead of hashing the whole contents of each file, we hashed three
    fixed-size "samples" from each file made of the first xx bytes, the middle
    xx bytes, and the last xx bytes? This would let us fingerprint a file in
    constant time!"""
    
    # My super-hip Macintosh uses a file system called HFS+, which has a default
    # block size of 4Kb (4,000 bytes) per block.
    num_bytes_to_read_per_sample = 4000

    # Return the size, in bytes, of path.
    total_bytes = os.path.getsize(path)

    # secure hash algorithm (SHA) with 512-bit hash values
    hasher = hashlib.sha512()

    with open(path, 'rb') as file:
        # if the file is too short to take 3 samples, hash the entire file
        if total_bytes < num_bytes_to_read_per_sample * 3:
            # Update the hash object with the string arg
            hasher.update(file.read())

        else:
            num_bytes_between_samples = (total_bytes - num_bytes_to_read_per_sample * 3) / 2

            # read first, middle, and last bytes
            for offset_multiplier in xrange(3):
                start_of_sample = offset_multiplier * (num_bytes_to_read_per_sample + num_bytes_between_samples)
                # To change the file object position, use f.seek(offset, from_what)
                file.seek(start_of_sample)
                # size is an optional numeric argument for .read().
                # When size is omitted or negative, the entire contents of the
                # file will be read and returned; it is your problem if the file
                # is twice as large as your machines memory. Otherwise, at most
                # size bytes are read and returned
                sample = file.read(num_bytes_to_read_per_sample)
                hasher.update(sample)

    # digest() returns the digest of the strings passed to the update() method
    # so far. This is a string of digest_size bytes which may contain non-ASCII 
    # characters, including null bytes. hexdigest() is similar.
    return hasher.hexdigest()




