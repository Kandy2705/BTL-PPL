# Generated from main/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_type.
    def visitStruct_type(self, ctx:MiniGoParser.Struct_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#data_struct.
    def visitData_struct(self, ctx:MiniGoParser.Data_structContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#initialize_struct.
    def visitInitialize_struct(self, ctx:MiniGoParser.Initialize_structContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_type.
    def visitInterface_type(self, ctx:MiniGoParser.Interface_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#data_inter.
    def visitData_inter(self, ctx:MiniGoParser.Data_interContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#initialize_inter.
    def visitInitialize_inter(self, ctx:MiniGoParser.Initialize_interContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#data_inter_thamso.
    def visitData_inter_thamso(self, ctx:MiniGoParser.Data_inter_thamsoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#global_variable.
    def visitGlobal_variable(self, ctx:MiniGoParser.Global_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#global_constant.
    def visitGlobal_constant(self, ctx:MiniGoParser.Global_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function.
    def visitFunction(self, ctx:MiniGoParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#data_func.
    def visitData_func(self, ctx:MiniGoParser.Data_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#body_func.
    def visitBody_func(self, ctx:MiniGoParser.Body_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_func.
    def visitAssignment_func(self, ctx:MiniGoParser.Assignment_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_else.
    def visitIf_else(self, ctx:MiniGoParser.If_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_basic.
    def visitFor_basic(self, ctx:MiniGoParser.For_basicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_icu.
    def visitFor_icu(self, ctx:MiniGoParser.For_icuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_range.
    def visitFor_range(self, ctx:MiniGoParser.For_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_func.
    def visitStruct_func(self, ctx:MiniGoParser.Struct_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call_str.
    def visitFunc_call_str(self, ctx:MiniGoParser.Func_call_strContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call_thamso_str.
    def visitFunc_call_thamso_str(self, ctx:MiniGoParser.Func_call_thamso_strContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_array.
    def visitType_array(self, ctx:MiniGoParser.Type_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_type_arr.
    def visitList_type_arr(self, ctx:MiniGoParser.List_type_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expr.
    def visitList_expr(self, ctx:MiniGoParser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#data_list_expr.
    def visitData_list_expr(self, ctx:MiniGoParser.Data_list_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#type_data.
    def visitType_data(self, ctx:MiniGoParser.Type_dataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_elements.
    def visitList_elements(self, ctx:MiniGoParser.List_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_expression.
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr1.
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr2.
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr3.
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr4.
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr5.
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr6.
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call.
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_call_thamso.
    def visitFunc_call_thamso(self, ctx:MiniGoParser.Func_call_thamsoContext):
        return self.visitChildren(ctx)



del MiniGoParser