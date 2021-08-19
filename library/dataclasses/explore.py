from dataclasses import dataclass, asdict, astuple


@dataclass
class Article:
    title: str
    author: str
    language: str
    upvotes: int


article = Article('DataClasses', 'nikhil', 'Python', 0)
print(article)
print(asdict(article))
print(astuple(article))


@dataclass
class CircleArea:
    r: int
    pi: float = 3.14

    @property
    def area(self):
        return self.pi * (self.r ** 2)


nums = CircleArea(2)
print(nums.area)
