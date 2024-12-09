from dataclasses import dataclass


@dataclass
class Block:
    block_type: int
    files: list[int]
    space_length: int

    TYPE_FILE = 1
    TYPE_SPACE = 0


class Solution:
    def parse_blocks(self, data):
        disk_map = data[0]
        blocks = []  # [block_type, [file_id], space_length]

        block_type = Block.TYPE_FILE  # 0: space, 1: file
        file_id = 0
        space_count = 0
        space_idx = []

        for i in map(int, disk_map):
            if block_type == Block.TYPE_FILE:
                block = Block(
                    block_type=block_type,
                    files=[file_id] * i,
                    space_length=0,
                )
                blocks.append(block)
                file_id += 1
            else:
                if i > 0:
                    space_count += i
                    space_idx.append(len(blocks))
                    block = Block(
                        block_type=block_type,
                        files=[],
                        space_length=i,
                    )
                    blocks.append(block)
            block_type = (block_type + 1) % 2

        return blocks, space_count, space_idx

    def part1(self, data):
        blocks, space_count, space_idx = self.parse_blocks(data)

        curr_block = []
        curr_space_idx = space_idx.pop(0)

        while space_count:
            if len(curr_block) == 0:
                if blocks[-1].block_type == Block.TYPE_SPACE and len(blocks[-1].files) == 0:
                    blocks.pop()
                    space_idx.pop()
                    continue

                if blocks[-1].block_type == Block.TYPE_FILE:
                    curr_block = blocks.pop().files

            try:
                item = curr_block.pop()
            except IndexError:
                break

            blocks[curr_space_idx].files.append(item)
            blocks[curr_space_idx].space_length -= 1
            space_count -= 1

            if blocks[curr_space_idx].space_length == 0:
                blocks[curr_space_idx].block_type = 1
                if space_idx:
                    curr_space_idx = space_idx.pop(0)
                else:
                    break

        if curr_block:
            blocks.append(
                Block(
                    block_type=Block.TYPE_FILE,
                    files=curr_block,
                    space_length=0,
                )
            )

        checksum = 0
        pos = 0
        for block in blocks:
            for file in block.files:
                checksum += pos * file
                pos += 1

        return checksum

    def part2(self, data):
        blocks, space_count, space_idx = self.parse_blocks(data)

        curr_block_idx = len(blocks) - 1

        while curr_block_idx > 0:
            if blocks[curr_block_idx].block_type == Block.TYPE_SPACE:
                curr_block_idx -= 1
                continue

            curr_block_len = len(blocks[curr_block_idx].files)
            for curr_space_idx in space_idx:
                if curr_space_idx >= curr_block_idx:
                    break

                if blocks[curr_space_idx].space_length >= curr_block_len:
                    # Move files to the space
                    blocks[curr_space_idx].files.extend(blocks[curr_block_idx].files)
                    blocks[curr_space_idx].space_length -= curr_block_len

                    # Mark current block as a space
                    blocks[curr_block_idx].block_type = Block.TYPE_SPACE
                    blocks[curr_block_idx].space_length = curr_block_len
                    blocks[curr_block_idx].files = []

                    # If the space is fully filled, remove it from the space index
                    if blocks[curr_space_idx].space_length == 0:
                        space_idx.remove(curr_space_idx)

                    break

            curr_block_idx -= 1

        checksum = 0
        pos = 0
        for block in blocks:
            for file in block.files:
                checksum += pos * file
                pos += 1
            if block.block_type == Block.TYPE_SPACE:
                pos += block.space_length

        return checksum


# Function to read the input from the file
def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]


# Main function to execute the solution
def main():
    # Read input from the file
    file_path = 'Datasets/dataset_day9.txt'  # You can change the path if needed
    data = read_input(file_path)
    
    # Initialize Solution and run the solution part 1
    solution = Solution()
    result_part1 = solution.part1(data)
    print(f"Checksum for Part 1: {result_part1}")
    
    # Run the solution part 2
    result_part2 = solution.part2(data)
    print(f"Checksum for Part 2: {result_part2}")


if __name__ == "__main__":
    main()
