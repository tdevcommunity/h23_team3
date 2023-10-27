import { StaticImport } from "next/dist/shared/lib/get-img-props";
import Image from "next/image"

const SliderCard: React.FC<{ url: any, profession: String,name: name }> = ({ url, profession, name}) => {
    return <div className="h-[18rem] w-[15rem] relative  rounded-3xl  overflow-hidden">
        <div className="absolute w-full h-full flex felx-col  items-end bg-black/20 ">
        <div className="text-white py-3 pl-3 ">
            <div className="text-lg">{name}</div>
      <span className="border py-1 rounded-full px-2 mt-4 inline-block text-sm  ">
      {profession}
      </span>
        </div>
        </div>

        <Image
            className="w-full h-full object-cover"
            src={url}
            width={300}
            height={300}
            alt="" />
    </div>
}
export default SliderCard; 