import { SearchIcon } from "@/components/icon/icons";
import { LinkButtonSecondary, LinkButtonOutline } from "@/components/ui/linkButton";
import Image from "next/image";

export default function Ressources() {
    return <div className="">
        <section className="w-full py-20 bg-gray-100 flex flex-col  justify-center">
            <div className="w-10/12 mx-auto flex flex-col items-center">

                <div className="py-8 w-3/6  flex flex-col items-center  ">

                    <h1 className="text-6xl  leading-tight font-semibold">
                        Reste curieux.
                    </h1>
                    <p className="w-5/6 py-4  text-xl  text-center">
                        Découvrez les histoires, les réflexions et l'expertise d'écrivains sur n'importe quel sujet.

                    </p>
                    
                        <div className='w-4/6 mt-6 border flex m px-3 shadow-lg shadow-gray-500/10  rounded-md items-center bg-white '>
                            <SearchIcon />
                            <input className='h-14 px-5 border-0 group focus:outline-none focus:ring-0 ' type='text' placeholder="Rechercher" />
                        </div>
                    
                </div>
                <div className="inline-flex gap-8 ">

                </div>

            </div>
        </section>

        <section className="w-8/12 mx-auto  mt-10 ">
            <div className="grid grid-cols-6 w-full">
                <div className="col-span-4 h-screen p-6 ">
                    <div className="text-gray-600 text-lg mb-4 ">Les plus lus </div>
                    <div className="p-4 mb-3  border hover:border-xmentor  grid grid-cols-5 rounded hover:bg-xmentor/10  ">
                        <div className="col-span-4">
                           <div className="flex gap-4 items-center ">
                           <Image src="/assets/mentors/mentor1.jpg" height={50} width={50} alt="" className="rounded-full h-10 w-10" />
                            <span className=" text">Sarah belingue </span>
                           </div>
                           <div className="text-xl font-semibold mt-2 "> 18 Life Lessons I’d Give My 18-Year-Old Self</div>
                            <p className="line-clamp-3 text-sm text-gray-700 py-2 ">
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat quidem aperiam provident optio eos atque eaque quas. Dicta sequi, nisi, exercitationem aspernatur nihil fugiat nobis numquam tenetur magni obcaecati in?
                            </p>
                            <div>

                            </div>
                        </div>
                        <div>
                            <Image  src="/assets/illustrations/illustration.png" height={300} width={200} alt=""  className="w-40 h-40" />
                        </div>
                    </div>
                    <div className="p-4 mb-3  border hover:border-xmentor  grid grid-cols-5 rounded hover:bg-xmentor/10  ">
                        <div className="col-span-4">
                           <div className="flex gap-4 items-center ">
                           <Image src="/assets/mentors/mentor1.jpg" height={50} width={50} alt="" className="rounded-full h-10 w-10" />
                            <span className=" text">Sarah belingue </span>
                           </div>
                           <div className="text-xl font-semibold mt-2 "> 18 Life Lessons I’d Give My 18-Year-Old Self</div>
                            <p className="line-clamp-3 text-sm text-gray-700 py-2 ">
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat quidem aperiam provident optio eos atque eaque quas. Dicta sequi, nisi, exercitationem aspernatur nihil fugiat nobis numquam tenetur magni obcaecati in?
                            </p>
                            <div>

                            </div>
                        </div>
                        <div>
                            <Image  src="/assets/illustrations/illustration.png" height={300} width={200} alt=""  className="w-40 h-40" />
                        </div>
                    </div>
                    <div className="p-4 mb-3  border hover:border-xmentor  grid grid-cols-5 rounded hover:bg-xmentor/10  ">
                        <div className="col-span-4">
                           <div className="flex gap-4 items-center ">
                           <Image src="/assets/mentors/mentor1.jpg" height={50} width={50} alt="" className="rounded-full h-10 w-10" />
                            <span className=" text">Sarah belingue </span>
                           </div>
                           <div className="text-xl font-semibold mt-2 "> 18 Life Lessons I’d Give My 18-Year-Old Self</div>
                            <p className="line-clamp-3 text-sm text-gray-700 py-2 ">
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat quidem aperiam provident optio eos atque eaque quas. Dicta sequi, nisi, exercitationem aspernatur nihil fugiat nobis numquam tenetur magni obcaecati in?
                            </p>
                            <div>

                            </div>
                        </div>
                        <div>
                            <Image  src="/assets/illustrations/illustration.png" height={300} width={200} alt=""  className="w-40 h-40" />
                        </div>
                    </div>

                    <div className="p-4 mb-3  border hover:border-xmentor  grid grid-cols-5 rounded hover:bg-xmentor/10  ">
                        <div className="col-span-4">
                           <div className="flex gap-4 items-center ">
                           <Image src="/assets/mentors/mentor1.jpg" height={50} width={50} alt="" className="rounded-full h-10 w-10" />
                            <span className=" text">Sarah belingue </span>
                           </div>
                           <div className="text-xl font-semibold mt-2 "> 18 Life Lessons I’d Give My 18-Year-Old Self</div>
                            <p className="line-clamp-3 text-sm text-gray-700 py-2 ">
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat quidem aperiam provident optio eos atque eaque quas. Dicta sequi, nisi, exercitationem aspernatur nihil fugiat nobis numquam tenetur magni obcaecati in?
                            </p>
                            <div>

                            </div>
                        </div>
                        <div>
                            <Image  src="/assets/illustrations/illustration.png" height={300} width={200} alt=""  className="w-40 h-40" />
                        </div>
                    </div>
                    <div className="p-4 mb-3  border hover:border-xmentor  grid grid-cols-5 rounded hover:bg-xmentor/10  ">
                        <div className="col-span-4">
                           <div className="flex gap-4 items-center ">
                           <Image src="/assets/mentors/mentor1.jpg" height={50} width={50} alt="" className="rounded-full h-10 w-10" />
                            <span className=" text">Sarah belingue </span>
                           </div>
                           <div className="text-xl font-semibold mt-2 "> 18 Life Lessons I’d Give My 18-Year-Old Self</div>
                            <p className="line-clamp-3 text-sm text-gray-700 py-2 ">
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat quidem aperiam provident optio eos atque eaque quas. Dicta sequi, nisi, exercitationem aspernatur nihil fugiat nobis numquam tenetur magni obcaecati in?
                            </p>
                            <div>

                            </div>
                        </div>
                        <div>
                            <Image  src="/assets/illustrations/illustration.png" height={300} width={200} alt=""  className="w-40 h-40" />
                        </div>
                    </div>

                    <div className="p-4 mb-3  border hover:border-xmentor  grid grid-cols-5 rounded hover:bg-xmentor/10  ">
                        <div className="col-span-4">
                           <div className="flex gap-4 items-center ">
                           <Image src="/assets/mentors/mentor1.jpg" height={50} width={50} alt="" className="rounded-full h-10 w-10" />
                            <span className=" text">Sarah belingue </span>
                           </div>
                           <div className="text-xl font-semibold mt-2 "> 18 Life Lessons I’d Give My 18-Year-Old Self</div>
                            <p className="line-clamp-3 text-sm text-gray-700 py-2 ">
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat quidem aperiam provident optio eos atque eaque quas. Dicta sequi, nisi, exercitationem aspernatur nihil fugiat nobis numquam tenetur magni obcaecati in?
                            </p>
                            <div>

                            </div>
                        </div>
                        <div>
                            <Image  src="/assets/illustrations/illustration.png" height={300} width={200} alt=""  className="w-40 h-40" />
                        </div>
                    </div>




                </div>
                <div className="p-3  w-full col-span-2 ">
                    <div className=" font-medium text-lg mb-4 ">Découvrez davantage ce qui compte pour vous</div>
                    <div className="flex flex-wrap gap-4 ">
                        <LinkButtonOutline className="hover:bg-xmentor border-none bg-xmentor/10 text-black hover:text-white  h-10 px-3 font-light  text-sm " href={"#"}>
                            Flutter
                        </LinkButtonOutline>
                        <LinkButtonOutline className="hover:bg-xmentor border-none bg-xmentor/10 text-black hover:text-white  h-10 px-3 font-light  text-sm  " href={"#"}>
                            React js
                        </LinkButtonOutline>
                        <LinkButtonOutline className="hover:bg-xmentor border-none bg-xmentor/10 text-black hover:text-white  h-10 px-3 font-light  text-sm " href={"#"}>
                            Java
                        </LinkButtonOutline>
                        <LinkButtonOutline className="hover:bg-xmentor border-none bg-xmentor/10 text-black hover:text-white  h-10 px-3 font-light  text-sm " href={"#"}>
                            Kotlin
                        </LinkButtonOutline>
                        <LinkButtonOutline className="hover:bg-xmentor border-none bg-xmentor/10 text-black hover:text-white  h-10 px-3 font-light  text-sm " href={"#"}>
                            c#/c++
                        </LinkButtonOutline>
                        <LinkButtonOutline className="hover:bg-xmentor border-none bg-xmentor/10 text-black hover:text-white  h-10 px-3 font-light  text-sm  " href={"#"}>
                            Svelte
                        </LinkButtonOutline>
                        <LinkButtonOutline className="hover:bg-xmentor border-none bg-xmentor/10 text-black hover:text-white  h-10 px-3 font-light  text-sm " href={"#"}>
                            ASSEMBLY
                        </LinkButtonOutline>
                        <LinkButtonOutline className="hover:bg-xmentor border-none bg-xmentor/10 text-black hover:text-white  h-10 px-3 font-light  text-sm " href={"#"}>
                            Javascript
                        </LinkButtonOutline>
                    </div>

                </div>
            </div>
        </section>

    </div>

}