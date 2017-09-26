import Block
import pickle
import sys

# # add the genesis block
#
helptext = "Commands: \n \ncreate-blockchain - creates a new genesis node, and overwrites the existing blockchain \nadd-block - adds a new block to the blockchain\nshow-blockchain - displays the blockchain"

# if web enabled, I will need to change this
with open("theBlockChain.pkl", "rb") as input:
    blocks = pickle.load(input)

if len(sys.argv)==1:
    print(helptext)

elif len(sys.argv) == 2 and (str(sys.argv[1]) == "create-blockchain"):
    genesis_block = Block.Block(0, "0", "The Genesis Block.")
    blocks.push(genesis_block)
    with open("theBlockChain.pkl", "wb") as output:
        pickle.dump(blocks, output, pickle.HIGHEST_PROTOCOL)

elif len(sys.argv) == 2 and (str(sys.argv[1]) == "show-blockchain"):
    print("current blocks: " + str(blocks))

elif len(sys.argv) == 3 and (str(sys.argv[1]) == "add-block") :
    if len(blocks)==0:
        print("error, please type \"load-blockchain\" and try again")
    else:
        data = str(sys.argv[2])
        blocks.append(Block.Block(len(blocks), blocks[len(blocks)-1].hash, data))
        with open("theBlockChain.pkl", "wb") as output:
            pickle.dump(blocks, output, pickle.HIGHEST_PROTOCOL)

else:
    print("error, unknown command \n")
    print(helptext)