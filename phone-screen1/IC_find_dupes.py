import os
import hashlib

def find_duplicate_files(starting_directory='/tmp/test'):
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


def sample_hash_file(path):
    num_bytes_to_read_per_sample = 4000 # why?
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
                # To change the file object’s position, use f.seek(offset, from_what)
                file.seek(start_of_sample)
                # size is an optional numeric argument for .read().
                # When size is omitted or negative, the entire contents of the
                # file will be read and returned; it’s your problem if the file
                # is twice as large as your machine’s memory. Otherwise, at most
                # size bytes are read and returned
                sample = file.read(num_bytes_to_read_per_sample)
                hasher.update(sample)

    # digest() returns the digest of the strings passed to the update() method
    # so far. This is a string of digest_size bytes which may contain non-ASCII 
    # characters, including null bytes. hexdigest() is similar.
    return hasher.hexdigest()




