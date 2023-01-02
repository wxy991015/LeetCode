def numberOfBeams(bank: list[str]) -> int:
    laser_beams_nums = 0
    for i in range(len(bank)):
        security_devices_prev = bank[i].count("1")
        for j in range(i+1, len(bank)):
            security_devices_next = bank[j].count("1")
            if security_devices_next != 0:
                laser_beams_nums += security_devices_next * security_devices_prev
                break
    return laser_beams_nums

bank = ["000","111","000"]
print(f"Output: {numberOfBeams(bank)}")