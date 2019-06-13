import yaml
if __name__ == '__main__':
    with open('test.yaml') as f:
        content = yaml.load(f, Loader=yaml.RoundTripLoader)

        print(type(content))
        print(content)

        content.update({'age': 38})
        print(content)
