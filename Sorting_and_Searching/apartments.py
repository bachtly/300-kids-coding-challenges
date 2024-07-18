if __name__ == "__main__":
    n_applicants, n_apartments, delta = [int(i) for i in input().split()]
    applicants = [int(i) for i in input().split()]
    apartments = [int(i) for i in input().split()]

    applicants.sort()
    apartments.sort()

    result = 0
    applicant_idx, apartment_idx = 0, 0
    while applicant_idx < n_applicants and apartment_idx < n_apartments:
        # the apartment meets the requirement of the applicant
        if apartments[apartment_idx] - delta <= applicants[applicant_idx] <= apartments[apartment_idx] + delta:
            result += 1
            apartment_idx += 1
            applicant_idx += 1
            continue

        # the apartment is smaller
        if apartments[apartment_idx] + delta < applicants[applicant_idx]:
            apartment_idx += 1
            continue
        else:
            applicant_idx += 1
            continue

    print(result)
