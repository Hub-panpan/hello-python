package com.itheima12.spring.aop.xml.privilege.service.impl;

import com.itheima12.spring.aop.xml.privilege.annotation.PrivlegeInfo;
import com.itheima12.spring.aop.xml.privilege.service.PersonService;

public class PersonServiceImpl implements PersonService{
	//只有当前用户有权限的时候 才能有响应的方法
	//我这不关注权限
	//只标识 想访问呢我的方法 需要的权限
	//也不用判断了 判断出去了
	//所以说 这事松耦合的
	
	@PrivlegeInfo(name="savePerson")
	public void savePerson() {
		// TODO Auto-generated method stub
		System.out.println("save person");
	}

	@PrivlegeInfo(name="updatePerson")
	public void updatePerson() {
		// TODO Auto-generated method stub
		System.out.println("update person");
	}
}
