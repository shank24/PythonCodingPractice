class Handler: #Abstract Handler

    def __init__(self, successor):
        self.successor = successor # Define who is the next handler

    def handle(self, request):
        handled = self._handle(request) #If handled, stop here

        #Otherwise, keep going
        if not handled:
            self._successor.handle(request)

    def handle(self, request):
        raise NotImplementedError("Must provide implementation in subclass")


class ConcreteHandler1(Handler): #Inherits from the abstract handler
    '''Default Handler'''
    def handle(self,request):
        if 0 < request <=10: #provide a condition for handling
            print("Request {} handle in handler 1".format(request))
            return  True # Indicates that the request has been handled


class DefaultHandler(Handler): #Inherits from the abstract handler
    '''Default Handler'''
    def handle(self,request):
        '''If there is no handler available'''
        #No condition checking since this is a default handler
        print("End of Chain, no handler for {}".format(request))
        return  True # Indicates that the request has been handled



class Client: #Using Handlers
    def __init__(self):
        self.handler = ConcreteHandler1(DefaultHandler(None))
        #Create handlers and use them in a sequence you want
            #Note that default handler has no successor

    def delegate(self,requests): #Send your requests one at a time for handlers to handle
        for request in requests:
            self.handler.handle(request)


#Create client
c = Client()

#Create a Request
requests = [2,5,10]

#Send the request
c.delegate(requests)