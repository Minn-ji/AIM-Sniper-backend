from abc import ABC, abstractmethod


class ProductRepository(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, productName, productPrice, productCategory, content, productTitleImage):
        pass

    @abstractmethod
    def findByProdictIdList(self, productIdList):
        pass

    @abstractmethod
    def findAllByProductCategory(self, productCategory):
        pass