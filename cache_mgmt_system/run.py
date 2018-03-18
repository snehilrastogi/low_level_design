from level_wise_cache.services.cache_mgmt_service import CacheMgmtService

num_levels = 5
read_times = [1, 2, 3, 4, 5]
write_times = [2, 4, 6, 8, 10]

input_data = ['read: "abc"', 'write "abc" "def"', 'write "ghi" "jkl"', 'read "ghi"', 'write "abc" "pqr"']

if __name__ == "__main__":
    print("Running")
    cache_mgmt = CacheMgmtService(num_levels, read_times, write_times, input_data)
    cache_mgmt.run_cache_system()
