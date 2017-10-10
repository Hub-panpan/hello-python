package com.itheima12.spring.aop.xml.exception.aspect;

import org.aspectj.lang.JoinPoint;

/**
 * 说明：
 *     切面的通知是处理异常的，而这个异常处理是完全独立于系统之外的内容
 *     本身是架构 但是和action 和 service 都是脱离开的
 *     我是独特的我 但是我还是可以融合再一起的 
 *
 */
public class ExceptionAspect {
	//自己起的名字
	public void throwingExcetion(JoinPoint joinPoint,Throwable ex){
		//这里输出异常
		//有 了 spring 的异常通知以后 就可以脱离任何框架
		System.out.println(ex.getMessage());
	}
}
