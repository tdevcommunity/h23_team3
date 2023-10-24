import { ReactNode } from "react";
import { LinkButton } from "./linkButton";

interface SignUpCardProps {
    children: ReactNode;
  }
const SignUpCard: React.FC<SignUpCardProps> = ({children}) => {
    return  <div className=" w-4/6 bg-gray-100 group duration-300 hover:shadow-xl  hover:bg-gradient-to-tr hover:from-purple-500 hover:to-pink-500 p-1 rounded-[1.2rem] ">
    <div className="group-hover:bg-white  h-[20rem]  items-center flex  duration-300 bg-gray-100 py-10 px-10 rounded-2xl">
        <div>
        {children}
        </div>
        
    </div>

</div>
}
export  { SignUpCard };