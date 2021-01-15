import sys
import getopt
import os


def parse_data(in_dir: str, out_dir: str):

    # get files
    train_in: str = os.path.join(in_dir, 'train.csv')
    test_in: str = os.path.join(in_dir, 'test.csv')
    valid_in: str = os.path.join(in_dir, 'valid.csv')

    # output file
    train_out: str = os.path.join(out_dir, 'train.tsv')
    test_out: str = os.path.join(out_dir, 'test.tsv')
    valid_out: str = os.path.join(out_dir, 'dev.tsv')
    emo_out: str = os.path.join(out_dir, 'emotions.txt')

    f_train_in = open(train_in, 'r')
    f_test_in = open(test_in, 'r')
    f_valid_in = open(valid_in, 'r')

    f_train_out = open(train_out, 'w')
    f_test_out = open(test_out, 'w')
    f_valid_out = open(valid_out, 'w')
    f_emo_out = open(emo_out, 'w')

    emotion_count: dict(str, int) = {i: 0 for i in range(16)}
    emotion_ids: dict(str, int) = {
        'angry': 0,
        'furious': 0,
        'grateful': 1,
        'trusting': 1,
        'jealous': 2,
        'ashamed': 2,
        'guilty': 3,
        'apprehensive': 3,
        'disappointed': 4,
        'disgusted': 4,
        'faithful': 5,
        'confident': 5,
        'annoyed': 6,
        'devastated': 6,
        'surprised': 7,
        'anticipating': 7,
        'joyful': 8,
        'excited': 8,
        'proud': 9,
        'hopeful': 9,
        'embarrassed': 10,
        'anxious': 10,
        'sad': 11,
        'lonely': 11,
        'afraid': 12,
        'terrified': 12,
        'caring': 13,
        'content': 13,
        'nostalgic': 14,
        'impressed': 14,
        'sentimental': 15,
        'prepared': 15
    }

    for file_in, file_out in zip([f_train_in, f_test_in, f_valid_in], [f_train_out, f_test_out, f_valid_out]):

        for line_num, line_data in enumerate(file_in):

            if line_num == 0:
                continue

            [conv_id, conv_idx, emotion, prompt, __, text] = \
                line_data.split(',')[:6]

            if int(conv_idx) % 2 == 1:

                if emotion not in emotion_ids:
                    print(f'Missed {emotion}')
                else:
                    emotion_count[emotion_ids[emotion]] += 1

                new_line = f'{process_text(text, prompt, file_in.name, line_num)}\t{emotion_ids[emotion]}\t{conv_id}_{conv_idx}\n'
                file_out.write(new_line)

    emotions = [''] * len(emotion_ids)
    for emotion, id in emotion_ids.items():
        emotions[id] += emotion

    for idx, emotion in enumerate(emotions):
        f_emo_out.write(emotion)
        if idx != len(emotions) - 1:
            f_emo_out.write('\n')

    f_train_in.close()
    f_test_in.close()
    f_valid_in.close()
    f_train_out.close()
    f_test_out.close()
    f_valid_out.close()
    f_emo_out.close()
    print(emotion_count)


def process_text(text: str, prompt: str, filename: str, line_num: int):
    text = text.strip()
    if text[0] == "\"" and "\"Super Shot Brothers\"" != text[:21]:
        text = text[1:]
        if text[-1] == "\"":
            text = text[:-1]
        elif len(text) >= 2 and text[-2] == "\"":
            text = text[:-2]
        print(text, filename, line_num)
    elif text.count('\"') % 2 == 1:
        if text[-1] == "\"":
            text = text[:-1]
        elif len(text) >= 2 and text[-2] == "\"":
            text = text[:-2]
        print(text, filename, line_num)

    return text.replace('_comma_', ',').replace(' ,', ',').replace(' .', '.').replace(' ?', '?').replace(' !', '!').strip()


def main(argv):

    in_dir = ''
    out_dir = ''

    try:
        opts, args = getopt.getopt(argv, "h:i:o:", ["in_dir=", "out_dir="])
    except getopt.GetoptError:
        print("python3 parser.py -i <in_dir> -o <out_dir>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("python3 parser.py -i <in_dir> -o <out_dir>")
            sys.exit()
        elif opt in ("-i", "--in_dir"):
            in_dir = arg
        elif opt in ("-o", "--out_dir"):
            out_dir = arg

    print("Input directory : ", in_dir)
    print("Ouptut directory: ", out_dir)

    parse_data(in_dir, out_dir)


if __name__ == '__main__':
    main(sys.argv[1:])
