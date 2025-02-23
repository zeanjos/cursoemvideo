from time import sleep
import emoji
fogos = emoji.emojize(":sparkler:")
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('Fogos de artificios! {}'.format(fogos))
