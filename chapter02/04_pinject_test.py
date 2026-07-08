import pinject


class ChatClient:
    def __init__(self, connection):
        print(self, "GOT", connection)
        
class Connection:
    pass

class FakeConnection:
    pass

class FakeBindingSpec(pinject.BindingSpec):
    def provide_connection(self):
        return FakeConnection()

class PrototypeBindingSpec(pinject.BindingSpec):
    @pinject.provides(in_scope=pinject.PROTOTYPE)
    def provide_connection(self):
        return Connection()

injector = pinject.new_object_graph()
faked_injector = pinject.new_object_graph(binding_specs=[FakeBindingSpec()])
proto_injector = pinject.new_object_graph(binding_specs=[PrototypeBindingSpec()])

if __name__ == "__main__":
    cli = injector.provide(ChatClient)
    cli_fake = faked_injector.provide(ChatClient)
    cli_proto = proto_injector.provide(ChatClient)
    cli_round2 = injector.provide(ChatClient)