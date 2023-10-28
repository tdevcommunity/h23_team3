import { HomeIcon } from "@/components/icon/icons";
import { LinkButtonOutline } from "@/components/ui/linkButton";
import Image from "next/image";
import Link from "next/link";


export default function Dashboard() {
    return <section className="w-full lg:min-h-screen bg-gray-100 ">
        <div className="w-7/12 mx-auto   grid grid-cols-5 pt-10  ">
            <div className="w-full bg-white">
                <div className="border rounded ">
                    <ul className="">
                        <li className="bg-xmentor/10 cursor-pointer text-xmentor flex gap-4  items-center px-4 py-2 rounded  ">
                            <span>
                                <HomeIcon />
                            </span>
                            <span>
                                Dashbord
                            </span>
                        </li>
                        <li className=" cursor-pointer hover:bg-gray-100 duration-200 flex gap-4  items-center px-4 py-2 rounded  ">
                            <span>
                                <HomeIcon />
                            </span>
                            <span>
                                Me questions
                            </span>
                        </li>
                        <li className="  cursor-pointer  flex gap-4 duration-200  hover:bg-gray-100  items-center px-4 py-2 rounded  ">
                            <span>
                                <HomeIcon />
                            </span>
                            <span>
                                Sessions
                            </span>
                        </li>
                        <li className="  cursor-pointer  flex gap-4 duration-200  hover:bg-gray-100  items-center px-4 py-2 rounded  ">
                            <span>
                                <HomeIcon />
                            </span>
                            <span>
                                Code reviews
                            </span>
                        </li>
                        <li className="  cursor-pointer  flex gap-4 duration-200  hover:bg-gray-100  items-center px-4 py-2 rounded  ">
                            <span>
                                <HomeIcon />
                            </span>
                            <span>
                                FAQ
                            </span>
                        </li>
                    </ul>
                </div>
            </div>
            <div className="col-span-3 w-full  p-5 h-full ">
                <div className="">
                    <div>
                        <span className="text-xl font-medium"> Suggestion de mentors</span>
                        <p className="text-sm  text-gray-500">
                            Ses mentors sont proposés en fonciton de votre profil
                        </p>
                        <div className="flex gap-2 flex-col mt-5 ">
                            <div className="flex items-center gap-3 bg-white  p-2 rounded border ">
                                <Image className="rounded-full w-12 h-12 object-cover" src="/assets/mentors/mentor1.jpg" height={80} width={80} alt="" />
                               <div className="flex justify-between items-center w-full ">
                                 <span className="font-medium">Sarah Mépigan</span>
                                <LinkButtonOutline className="h-10 text-sm " href={""}>
                                    Voir plus
                                </LinkButtonOutline>
                               </div>
                            </div>
                            <div className="flex items-center gap-3 bg-white  p-2 rounded border ">
                                <Image className="rounded-full w-12 h-12 object-cover" src="/assets/mentors/mentor1.jpg" height={80} width={80} alt="" />
                               <div className="flex justify-between items-center w-full ">
                                 <span className="font-medium">Sarah Mépigan</span>
                                <LinkButtonOutline className="h-10 text-sm " href={""}>
                                    Voir plus
                                </LinkButtonOutline>
                               </div>
                            </div>
                              <div className="flex items-center gap-3 bg-white  p-2 rounded border ">
                                <Image className="rounded-full w-12 h-12 object-cover" src="/assets/mentors/mentor1.jpg" height={80} width={80} alt="" />
                               <div className="flex justify-between items-center w-full ">
                                 <span className="font-medium">Sarah Mépigan</span>
                                <LinkButtonOutline className="h-10 text-sm " href={""}>
                                    Voir plus
                                </LinkButtonOutline>
                               </div>
                            </div>
                        </div>
                    </div>
                    <div className="w-full ">

                    </div>
                </div>
            </div>
            <div className="w-full p-2 ">
                <div className=" font-medium ">Aide  et support </div>
                <ul className="flex gap-3 flex-col mt-2 text-xmentor">
                    <li>
                        <Link className="underline text-sm " href={"#"} passHref>Trouver des ressources</Link>
                    </li>
                    <li>
                        <Link className="underline text-sm " href={"#"} passHref>contacter pur assistance</Link>
                    </li>
                    <li>
                        <Link className="underline text-sm " href={"#"} passHref>Partager un avis </Link>

                    </li>

                </ul>
            </div>
        </div>
    </section>
}

Dashboard.getLayout = function (page: any) {
    return <body>{page}</body>;
};