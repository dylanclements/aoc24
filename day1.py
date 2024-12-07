def main() -> None:
    left: list[int] = []
    right: list[int] = []
    with open('day1.txt', 'r') as fp:
        for line in fp:
            l, r= line.split("   ")
            left.append(int(l));
            right.append(int(r.strip()))

    freq_right = {}
    for r in right:
        freq_right.update({ r: freq_right[r] + 1 if r in freq_right else 1 })

    similarity_score = 0;
    for l in left:
        if l in freq_right:
            similarity_score += l * freq_right[l]

    print(similarity_score)


if __name__ == "__main__":
    main()
